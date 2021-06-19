library(effectsize)

rm(list = ls())
setwd("~/Dropbox/Research/Visual aesthetics/Politician/")
o <- data.frame(read.table(file="img attr/img aesthetics.txt", header=TRUE, quote = "\"", sep="\t"))
colnames(o)
o[o == -99999] <- NA
dc = o

tvars = c("gray_mean",
          "contrast_range",
          "colorful",
          "hue_count",
          "file_size_s","edge_density","edge_distance","edge_box_size",
          "sharp_laplacian",
          "dof_inner")

t_test_stat <- function(var, dcompare) {
tformula = as.formula(paste(var,"~user"))
tr = t.test(tformula, data = dcompare)
er = effectsize(tr)
tstat = tr$statistic; m1 = tr$estimate[1];  m2 = tr$estimate[2]; df = tr$parameter; p = tr$p.value
cd = er$d
trow = list(var, m1, m2, tstat, df, p, cd)
return(trow)}

rtable = NULL

for (var in tvars) {
  print(var)
  rrow = t_test_stat(var, dc)
  rtable = rbind(rtable,rrow)
}

rtable