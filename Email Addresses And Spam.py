import ply.lex as lex
import re 

def addresses(haystack):
    
    tem = re.sub(r"NOSPAM", "", haystack) 
    
    return re.findall(r"[a-zA-Z]+@[a-zA-Z]+(?:\.[a-zA-Z]+)+",tem)    # attention, address may be XXX@xxx.xxx.xxx

input1 = """louiseNOSPAMaston@germany.de (1814-1871) was an advocate for
democracy. irmgardNOSPAMkeun@NOSPAMweimar.NOSPAMde (1905-1982) wrote about
the early nazi era. rahelNOSPAMvarnhagen@berlin.de was honored with a 1994
deutsche bundespost stamp. seti@home is not actually an email address."""

output1 = ['louiseaston@germany.de', 'irmgardkeun@weimar.de', 'rahelvarnhagen@berlin.de']

print (addresses(input1) == output1)
