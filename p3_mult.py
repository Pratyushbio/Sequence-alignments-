import pandas as pd
import os


CDict = { 
       'TTT': 0.0, 'TTC': 0.0, 'TTA': 0.0, 'TTG': 0.0, 'CTT': 0.0, 
       'CTC': 0.0, 'CTA': 0.0, 'CTG': 0.0, 'ATT': 0.0, 'ATC': 0.0, 
       'ATA': 0.0, 'ATG': 0.0, 'GTT': 0.0, 'GTC': 0.0, 'GTA': 0.0, 
       'GTG': 0.0, 'TAT': 0.0, 'TAC': 0.0, 'TAA': 0.0, 'TAG': 0.0, 
       'CAT': 0.0, 'CAC': 0.0, 'CAA': 0.0, 'CAG': 0.0, 'AAT': 0.0, 
       'AAC': 0.0, 'AAA': 0.0, 'AAG': 0.0, 'GAT': 0.0, 'GAC': 0.0, 
       'GAA': 0.0, 'GAG': 0.0, 'TCT': 0.0, 'TCC': 0.0, 'TCA': 0.0, 
       'TCG': 0.0, 'CCT': 0.0, 'CCC': 0.0, 'CCA': 0.0, 'CCG': 0.0, 
       'ACT': 0.0, 'ACC': 0.0, 'ACA': 0.0, 'ACG': 0.0, 'GCT': 0.0, 
       'GCC': 0.0, 'GCA': 0.0, 'GCG': 0.0, 'TGT': 0.0, 'TGC': 0.0, 
       'TGA': 0.0, 'TGG': 0.0, 'CGT': 0.0, 'CGC': 0.0, 'CGA': 0.0, 
       'CGG': 0.0, 'AGT': 0.0, 'AGC': 0.0, 'AGA': 0.0, 'AGG': 0.0, 
       'GGT': 0.0, 'GGC': 0.0, 'GGA': 0.0, 'GGG': 0.0}
	   
Fixed_values = {'TTT': {'Sti': 1, 'Stv': 0, 'Nsti': 2, 'Nstv': 6}, 
				'TTC': {'Sti': 1, 'Stv': 0, 'Nsti': 2, 'Nstv': 6}, 
				'TTA': {'Sti': 2, 'Stv': 0, 'Nsti': 1, 'Nstv': 4}, 
				'TTG': {'Sti': 2, 'Stv': 0, 'Nsti': 1, 'Nstv': 5}, 
				'CTT': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 4}, 
				'CTC': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 4}, 
				'CTA': {'Sti': 2, 'Stv': 2, 'Nsti': 1, 'Nstv': 4}, 
				'CTG': {'Sti': 2, 'Stv': 2, 'Nsti': 1, 'Nstv': 4}, 
				'ATT': {'Sti': 1, 'Stv': 1, 'Nsti': 2, 'Nstv': 5}, 
				'ATC': {'Sti': 1, 'Stv': 1, 'Nsti': 2, 'Nstv': 5}, 
				'ATA': {'Sti': 0, 'Stv': 2, 'Nsti': 3, 'Nstv': 4}, 
				'ATG': {'Sti': 0, 'Stv': 0, 'Nsti': 3, 'Nstv': 6}, 
				'GTT': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 4}, 
				'GTC': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 4}, 
				'GTA': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 4}, 
				'GTG': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 4}, 
				'TCT': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 4}, 
				'TCC': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 4}, 
				'TCA': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 2}, 
				'TCG': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 3}, 
				'CCT': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 4}, 
				'CCC': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 4}, 
				'CCA': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 4}, 
				'CCG': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 4}, 
				'ACT': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 4}, 
				'ACC': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 4}, 
				'ACA': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 4}, 
				'ACG': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 4}, 
				'GCT': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 4}, 
				'GCC': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 4}, 
				'GCA': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 4}, 
				'GCG': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 4}, 
				'TAT': {'Sti': 1, 'Stv': 0, 'Nsti': 2, 'Nstv': 4}, 
				'TAC': {'Sti': 1, 'Stv': 0, 'Nsti': 2, 'Nstv': 4}, 
				'CAT': {'Sti': 1, 'Stv': 0, 'Nsti': 2, 'Nstv': 6}, 
				'CAC': {'Sti': 1, 'Stv': 0, 'Nsti': 2, 'Nstv': 6}, 
				'CAA': {'Sti': 1, 'Stv': 0, 'Nsti': 1, 'Nstv': 6}, 
				'CAG': {'Sti': 1, 'Stv': 0, 'Nsti': 1, 'Nstv': 6}, 
				'AAT': {'Sti': 1, 'Stv': 0, 'Nsti': 2, 'Nstv': 6}, 
				'AAC': {'Sti': 1, 'Stv': 0, 'Nsti': 2, 'Nstv': 6}, 
				'AAA': {'Sti': 1, 'Stv': 0, 'Nsti': 2, 'Nstv': 5}, 
				'AAG': {'Sti': 1, 'Stv': 0, 'Nsti': 2, 'Nstv': 5}, 
				'GAT': {'Sti': 1, 'Stv': 0, 'Nsti': 2, 'Nstv': 6}, 
				'GAC': {'Sti': 1, 'Stv': 0, 'Nsti': 2, 'Nstv': 6}, 
				'GAA': {'Sti': 1, 'Stv': 0, 'Nsti': 2, 'Nstv': 5}, 
				'GAG': {'Sti': 1, 'Stv': 0, 'Nsti': 2, 'Nstv': 5}, 
				'TGT': {'Sti': 1, 'Stv': 0, 'Nsti': 2, 'Nstv': 5}, 
				'TGC': {'Sti': 1, 'Stv': 0, 'Nsti': 2, 'Nstv': 5}, 
				'TGG': {'Sti': 0, 'Stv': 0, 'Nsti': 1, 'Nstv': 6}, 
				'CGT': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 4}, 
				'CGC': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 4}, 
				'CGA': {'Sti': 1, 'Stv': 3, 'Nsti': 1, 'Nstv': 3}, 
				'CGG': {'Sti': 1, 'Stv': 3, 'Nsti': 2, 'Nstv': 3}, 
				'AGT': {'Sti': 1, 'Stv': 0, 'Nsti': 2, 'Nstv': 6}, 
				'AGC': {'Sti': 1, 'Stv': 0, 'Nsti': 2, 'Nstv': 6}, 
				'AGA': {'Sti': 1, 'Stv': 1, 'Nsti': 2, 'Nstv': 4}, 
				'AGG': {'Sti': 1, 'Stv': 1, 'Nsti': 2, 'Nstv': 5}, 
				'GGT': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 4}, 
				'GGC': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 4}, 
				'GGA': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 3}, 
				'GGG': {'Sti': 1, 'Stv': 2, 'Nsti': 2, 'Nstv': 4}}
				
SynonymousCodons = { 
       'CYS': ['TGT', 'TGC'], 
       'ASP': ['GAT', 'GAC'], 
       'SER': ['TCT', 'TCG', 'TCA', 'TCC', 'AGC', 'AGT'], 
       'GLN': ['CAA', 'CAG'], 
       'MET': ['ATG'], 
       'ASN': ['AAC', 'AAT'], 
       'PRO': ['CCT', 'CCG', 'CCA', 'CCC'], 
       'LYS': ['AAG', 'AAA'], 
    
       'THR': ['ACC', 'ACA', 'ACG', 'ACT'], 
       'PHE': ['TTT', 'TTC'], 
       'ALA': ['GCA', 'GCC', 'GCG', 'GCT'], 
       'GLY': ['GGT', 'GGG', 'GGA', 'GGC'], 
       'ILE': ['ATC', 'ATA', 'ATT'], 
       'LEU': ['TTA', 'TTG', 'CTC', 'CTT', 'CTG', 'CTA'], 
       'HIS': ['CAT', 'CAC'], 
       'ARG': ['CGA', 'CGC', 'CGG', 'CGT', 'AGG', 'AGA'], 
       'TRP': ['TGG'], 
       'VAL': ['GTA', 'GTC', 'GTG', 'GTT'], 
       'GLU': ['GAG', 'GAA'], 
       'TYR': ['TAT', 'TAC'] 
  }

def calculate_codon(sequence):            
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i + 3]
        if codon in CDict:
            CDict[codon] += 1
    return(CDict)
        

def ti_tv_fn(mx, tt):
    for i in range(len(mx)):
        if mx[i]!= tt[i]:
            #print(tt[i])
            if mx[i] == "A" and tt[i] == "G" or mx[i] == "G" and tt[i] == "A":
                ti_tv = "ti"
            elif mx[i] == "T" and tt[i] == "C" or mx[i] == "C" and tt[i] == "T":
                ti_tv = "ti" 
            else:
                ti_tv = "tv"
            return ti_tv
                    
def get_key(val):
    for key, value in SynonymousCodons.items():
        if val in value:
            return(key)

def S_Ns_ti_tv_fn(ti_tv, mx, tt):
    if(ti_tv):
        mx_key = get_key(mx)
        tt_key = get_key(tt)
        if mx_key == tt_key:
            Syn_NSyn = 'Syn'
        else:
            Syn_NSyn = 'NSyn'
        S_Ns_ti_tv = Syn_NSyn + ti_tv
        return(S_Ns_ti_tv)

def diff(mx, lst):
    pos = []
    for item in lst:
        diff_positions = [i for i in range(len(mx)) if mx[i] != item[i]]
        if len(diff_positions) > 1:
            return False
        elif len(diff_positions) == 1:
            pos.append(diff_positions[0])
    #print(pos)
    if (len(list(set(pos)))==1):
        return True
    else:
        return False
        
def divide_safely(a, b):
    try:
        if a is not None and b is not None and b!=0 :
            result = a / b
            return result
        else:
            return None
    except ZeroDivisionError:
        #print("Error: Division by zero is not allowed.")
        return None




def process(gene_names):
    ti_tv_values = []
    mutation = []
    df = pd.DataFrame()
    df_mut = pd.DataFrame()
    mut_cols = ["Gene","pos","fr_cdn","to_cdn","fr_AA","to_AA","Synti_Syntv_NSynti_NSyntv"]
    OE_values = []
    df_oe = pd.DataFrame()
    oe_cols = ["Gene", "Synti_o", "Syntv_o", "NSynti_o", "NSyntv_o", "ti_o", "tv_o", "Synti_e", "Syntv_e", "NSynti_e", "NSyntv_e", "ti_e", "tv_e"]
    reference_seq = []
    df_rsq = pd.DataFrame()
    rsq_cols = ["Gene","Reference Sequence"] 
    #gene_names = gene_names[:-1]
    for line in gene_names:
        line = line.strip("\n")
        fil_ = os.path.basename(line)
        file = os.path.splitext(fil_)[0]
			
        aa = open(line,"r")

        read_file = aa.read()
        N1 = read_file.count(">") # count number of strains
        read_file_split = read_file.split("\n")
        N = len(read_file_split[1]) # gene length
        #print(N, N1)



        # collect only strains in a list
        Only_strain = []

        for g in range(N1*2):
            if g%2 != 0:
                read_file_split[g] = read_file_split[g].upper().replace("U","T")
                Only_strain.append(read_file_split[g])
        #print(Only_strain)





        Synti = 0
        NSynti = 0
        Syntv = 0
        NSyntv = 0
        m_lst = []
        lst = []
        ref_seq = ''
        for j in range(0, N, 3):
            for i in range(N1):
                cdn = Only_strain[i][j:j+3] #column wise codon
                m_lst.append(cdn) # m_lst stores all codons in a list
                #print(m_lst)
            mx = max_occurred_element = max(set(m_lst), key=m_lst.count) # reference codon
            ref_seq += (mx) 
            lst_h = list(set(m_lst)) #find unique elements in list
            lst = [item for item in lst_h if item != mx and 'N' not in item]
            #print(lst)
            #print(mx)
            result = diff(mx, lst)
            #print(result)
            if (result):
                for tt in lst:
                    if tt== 'TGA' or tt == 'TAG' or tt == 'TAA' or 'N' in tt:
                        #print(tt)
                        continue
                    else:
                        ti_tv = ti_tv_fn(mx, tt)
                        S_Ns_ti_tv = S_Ns_ti_tv_fn(ti_tv, mx, tt)
                        #print(S_Ns_ti_tv)
                        
                        if(S_Ns_ti_tv):
                            mx_key = get_key(mx)
                            tt_key = get_key(tt)
                            mutation.append([file, str(j+1),mx,tt,mx_key, tt_key,S_Ns_ti_tv])
                            df_mut = pd.DataFrame(mutation, columns=mut_cols)
                            if S_Ns_ti_tv == 'Synti':
                                Synti += 1
                            elif S_Ns_ti_tv == 'NSynti':
                                NSynti += 1
                            elif S_Ns_ti_tv == 'Syntv':
                                Syntv += 1
                            elif S_Ns_ti_tv == 'NSyntv':
                                NSyntv += 1


            lst = []
            m_lst = []
            
        reference_seq.append([file, ref_seq])
        df_rsq = pd.DataFrame(reference_seq, columns = rsq_cols)           
        calculate_codon(ref_seq)
        with open('codon_count.txt', 'w') as ff:
            for codon, values in CDict.items():
                line = f"{codon}\t{values}\n"
                ff.write(line)	
        

        ti_o = Synti + NSynti
        tv_o = Syntv + NSyntv



        new_dict = {
            key: {inner_key: Fixed_values[key][inner_key] * CDict[key] for inner_key in Fixed_values[key]}
            for key in Fixed_values if key in CDict
        }


        #print(new_dict)

        Synti_e = sum(v['Sti'] for v in new_dict.values())
        Syntv_e = sum(v['Stv'] for v in new_dict.values())
        NSynti_e = sum(v['Nsti'] for v in new_dict.values())
        NSyntv_e = sum(v['Nstv'] for v in new_dict.values())

        ti_e = Synti_e + NSynti_e
        tv_e = Syntv_e + NSyntv_e
        
        OE_values.append([file, Synti, Syntv, NSynti, NSyntv, ti_o, tv_o, Synti_e, Syntv_e, NSynti_e, NSyntv_e, ti_e, tv_e])
        df_oe = pd.DataFrame(OE_values, columns=oe_cols)
        #print(Synti_e, Syntv_e, NSynti_e, NSyntv_e, ti_e, tv_e)
        #print(Synti, Syntv, NSynti, NSyntv, ti_o, tv_o)
        
        #Syntio_tvo
        result = divide_safely(Synti, Syntv)
        if result is not None:
            Stio_by_Stvo = str(round(result,3))
        else:
            Stio_by_Stvo = "Denominator is 0"
        
        #NSyntio_tvo
        result1 =  divide_safely(NSynti, NSyntv)       
        if result1 is not None:
            Ntio_by_Ntvo = str(round(result1,3))
        else:
            Ntio_by_Ntvo = "Denominator is 0"
        
        #tio_tvo
        result2 = divide_safely(ti_o, tv_o)
        if result2 is not None:
            tio_by_tvo = str(round(result2,3))
        else:
            tio_by_tvo = "Denominator is 0"
        

        #ti'/tv'
        result3 = divide_safely(ti_o, ti_e)
        result4 = divide_safely(tv_o, tv_e)
        rs = divide_safely(result3, result4)
        
        if rs is not None and result3 is not None and result4 is not None:
            ti_dash_by_tv_dash = str(round(rs,3))
        else:
            ti_dash_by_tv_dash = "Denominator is 0"
            
        #Sti'/Stv'
        result5 = divide_safely(Synti, Synti_e)
        result6 = divide_safely(Syntv, Syntv_e)
        rs1 = divide_safely(result5, result6)
        if rs1 is not None and result5 is not None and result6 is not None:
            Sti_dash_by_Stv_dash = str(round(rs1,3))
        else:
            Sti_dash_by_Stv_dash = "Denominator is 0"
        
        #Nti'/Ntv'
        result7 = divide_safely(NSynti, NSynti_e)
        result8 = divide_safely(NSyntv, NSyntv_e)
        rs2 = divide_safely(result7, result8)
        if rs2 is not None and result7 is not None and result8 is not None:
            Nti_dash_by_Ntv_dash = str(round(rs2,3))
        else:
            Nti_dash_by_Ntv_dash = "Denominator is 0"
            
        #print(round(Stio_by_Stvo,3), round(Ntio_by_Ntvo,3), round(tio_by_tvo,3), round(ti_dash_by_tv_dash,3), round(Sti_dash_by_Stv_dash,3), round(Nti_dash_by_Ntv_dash,3))
        ti_tv_values.append([file, Stio_by_Stvo, Ntio_by_Ntvo, tio_by_tvo, ti_dash_by_tv_dash, Sti_dash_by_Stv_dash, Nti_dash_by_Ntv_dash])
        
    
    columns = ["Gene","Stio / Stvo", "Ntio / Ntvo", "tio / tvo", "ti\' / tv\'", "Sti\' / Stv\'", "Nti\' / Ntv\'"]
    df = pd.DataFrame(ti_tv_values, columns=columns)
    return 	df, df_mut, df_oe, df_rsq