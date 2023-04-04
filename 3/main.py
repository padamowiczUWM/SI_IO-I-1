from scipy import stats

years = [2000, 2002, 2005, 2007, 2010]
percentage = [6.5, 7.0, 7.4, 8.2, 9.0]

slope, intercept, r_value, p_value, std_err = stats.linregress(years, percentage)

print("Równanie regresji liniowej: y = {:.3f}x + {:.3f}".format(slope, intercept))
print("R-kwadrat = {:.3f}".format(r_value**2))

year = (12 - intercept) / slope
print("Procent bezrobotnych przekroczy 12% w roku {:.0f}".format(year))