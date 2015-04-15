import numpy as np
import pylab as pyl

# allow user to input initial starting parameters 
p = float(raw_input('What is p? '))
wAA = float(raw_input('What is the homozygous dominant (AA) fitness? '))
wAa = float(raw_input('What is the heterozygote (Aa) fitness? '))
waa = float(raw_input('What is the homozygous recessive (aa) fitness? '))
t = int(raw_input('How many generations? '))

# change in allele frequencies as a function of genotypic fitness over time
def allelefit(p, wAA, wAa, waa, t):
    for i in range(0, t):
        q      =  1-p
        psq    =  p**2
        qsq    =  q**2
        twopq  =  2*p*q

        w = (psq * wAA) + (twopq * wAa) + (qsq * waa)

        psq_eff = ((psq * wAA) / w)
        twopq_eff = ((twopq * wAa) / w)
        qsq_eff = ((qsq * waa) / w)

        p = (psq_eff + (0.5 * twopq_eff))
        q = (qsq_eff + (0.5 * twopq_eff))

    return p, q


p, q = allelefit(p, wAA, wAa, waa, t)
w_new =  ((p**2 * wAA) + (2*p*(1-p) * wAa) + ((1-p)**2 * waa)) 
print "p =", p
print "q =", q
print "w =", w_new


# create plot of expected frequency of p for potential values of average fitness
f = lambda x : (x**2 * wAA) + (2*x*(1-x) * wAa) + ((1-x)**2 * waa)
p_range = np.arange(0, 1.01, 0.01)

pyl.plot(p_range, f(p_range))
pyl.plot(p, w_new, marker='o', color='r')  # put final value of p on this plot
pyl.title("Frequency of p")
pyl.xlabel("p")
pyl.ylabel("w")
pyl.show()
