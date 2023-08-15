import tkinter as tk
from tkinter import filedialog, messagebox
import os
import pandas as pd
import p3_mult
from pandastable import Table
import subprocess
from tkinter import scrolledtext

class Page(tk.Toplevel):
    def __init__(self, main_root, *args, **kwargs):
        super(Page, self).__init__(*args, **kwargs)
        self.title("Modified transition-transversion Calculator")
        self.geometry("700x400")
        self['background'] = 'thistle1'
        self.main_root = main_root  # Store a reference to the main window

        label_text = "Upload gene alignment file(s) in FASTA format"
        label = tk.Label(self, text=label_text, bg='thistle1', font=("Helvetica", 12), wraplength=200)
        label.grid(row=0, column=0, sticky="news", padx=15, pady=20)

        self.text_widget = tk.Text(self, width=30, height=10)
        self.text_widget.grid(row=0, column=1, sticky="news", padx=15, pady=35)

        browse_button = tk.Button(self, text="Browse", command=self.browse_files, font=("Helvetica", 14), bd='3')
        browse_button.grid(row=0, column=2, sticky="new", padx=15, pady=35)
        
        self.calculate_button = tk.Button(self, text="Calculate", font=("Helvetica", 14), bd='3', state=tk.DISABLED)
        self.calculate_button.grid(row=3, column=1, sticky="news", padx=15, pady=25)

        clear_button = tk.Button(self, text="Clear", command=self.clear_files, font=("Helvetica", 14), bd='3')
        clear_button.grid(row=0, column=3, sticky="new", padx=5, pady=35)

        how_to_use_button = tk.Button(self, text="How to Use", command=self.open_how_to_use, font=("Helvetica", 14), bd='3')
        how_to_use_button.grid(row=3, column=2, sticky="news", padx=15, pady=25)

    def on_gui_close(self):
        self.main_root.deiconify()  # Maximize the main window
        self.destroy()  # Close the gui.py interface    

    def is_fasta_format(self, file_path):
        with open(file_path, 'r') as file:
            line = file.readline()
            if line.startswith('>'):
                return True
            else:
                return False

    def browse_files(self):
        self.text_widget.delete("1.0", tk.END)

        filepaths = filedialog.askopenfilenames()
        self.files = []
        for filepath in filepaths:
            filename = os.path.basename(filepath)
            if self.is_fasta_format(filepath):
                self.files.append(filepath)
                self.text_widget.insert(tk.END, filename + "\n")
            else:
                messagebox.showwarning("Invalid File", f"{filename} is not in FASTA format. Please upload files in FASTA format only.")
        if self.files:
            self.calculate_button.config(command=self.on_calculate_button_click, state=tk.NORMAL)

    def clear_files(self):
        self.text_widget.delete("1.0", tk.END)
        self.calculate_button.config(command=None, state=tk.DISABLED)

    def open_how_to_use(self):
        how_to_use_text = """How to use the modified ti-tv calculator:

# Modified ti-tv Calculator

This software calculates the modified transition/transversion (ti-tv) values as described in the paper "Berua et al. 2023, Comparison between synonymous transition/transversion with non-synonymous transition/transversion reveals different purifying selection on coding sequences in Escherichia coli".

## Usage

1. **Upload Gene Alignment Files:**
   - From the main menu, click on the "ti-tv" tab and then select "ti-tv calculator".
   - Click the "Browse" button to upload one or more gene alignment files. The uploaded files should be in the multiple sequence alignment format of nucleic acids and have equal-length genes. You can refer to the provided "Sample_gene.txt" file in the folder as an example.

2. **Calculate Modified ti-tv Values:**
   - After uploading the gene alignment files, click on the "Calculate" button.
   - The software will calculate both the conventional ti-tv values and the modified ti-tv values for each individual gene.
   - Conventional ti-tv values are calculated from observed values of synonymous transition (Sti_o) or transversion (Stv_o), non-synonymous transition (Nti_o) or transversion (Ntv_o), and total transition (ti_o) or transversion (tv_o) ratios.
   - Modified ti-tv values (ti' and tv') are calculated using observed values and expected values (Sti_e, Stv_e, Nti_e, Ntv_e) as follows:
     - ti' / tv' = (ti_o / ti_e) / (tv_o / tv_e)
     - Sti' / Stv' = (Sti_o / Sti_e) / (Stv_o / Stv_e)
     - Nti' / Ntv' = (Nti_o / Nti_e) / (Ntv_o / Ntv_e)

3. **Clear Records:**
   - To clear all records and start over, click the "Clear" button.

## Supplementary Files
Three supplementary files will be created in Excel format in the same directory where the program is run:
- `result_data.xlsx`: Contains the calculated ti-tv values for each gene.
- `Supplementary_mutation_data.xlsx`: Supplementary mutation data.
- `Supplementary_observed_expected_values.xlsx`: Supplementary observed and expected values.
- `Supplementary_reference_seq.xlsx`: Supplementary reference sequences for each uploaded gene.

## Example Data
You can find an example gene alignment file named "Sample_gene.txt" in the folder, which you can use to test the calculator.

## Note
Make sure that all uploaded gene alignment files have equal-length genes to ensure accurate calculation of ti-tv values.

For any questions or issues, please refer to the paper or contact ssankar@tezu.ernet.in.
"""

        how_to_use_window = tk.Toplevel(self)
        how_to_use_window.title("How to Use")
		
        text_widget = scrolledtext.ScrolledText(how_to_use_window, wrap=tk.WORD, font=("Helvetica", 12), width=100, height=20)
        text_widget.insert(tk.END, how_to_use_text)
        text_widget.config(state=tk.DISABLED)
        text_widget.pack()


    def on_calculate_button_click(self):
        df, df_mut, df_oe, df_rsq = p3_mult.process(self.files)
        result_df = df

        result_df.to_excel("result_data.xlsx", index=False)
        df_mut.to_excel("Supplementary_mutation_data.xlsx", index=False)
        df_oe.to_excel("Supplementary_observed_expected_values.xlsx", index=False)
        df_rsq.to_excel("Supplementary_reference_seq.xlsx", index=False)

        # Display the result_df table using pandastable
        top_level = tk.Toplevel(self)
        top_level.title("Result Table")
        top_level_width = 800
        top_level.geometry(f"{top_level_width}x400")

        frame = tk.Frame(top_level)
        frame.pack(fill='both', expand=True)

        table = Table(frame, dataframe=result_df, showtoolbar=True, showstatusbar=True)
        table.show()
		
	

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("700x400")
    root.title("Modified transition-transversion Calculator")
    root['background'] = 'thistle1'

    gui = GUI(root)
    root.mainloop()