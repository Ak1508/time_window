
import string

with open("HMSADCGates.C", "r") as file:
    line = file.read()

# replace with 2ta, 3ta, 4ta, neg with pos 
line = line.replace("1pr", "2ta")

# line = line.replace("H_cer_adc", "H_cal_1pr_negAdc")
# line = line.replace("[2]", "[13]")
# line = line.replace("H_cer_good", "H_cal_1pr_goodNeg")

#line = line.replace("P_precal","H_cal_1pr")
#line = line.replace("P_hgcer", "H_cer")
#line = line.replace('*P','*H')
#line = line.replace("P_ngcer_good","P_precal_goodNeg")

with open("HMSADCGates.C", "w") as file:
    file.write(line)