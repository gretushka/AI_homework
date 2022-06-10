getwd()
#install.packages("rio")

library(rio)
?rio
#Сравним базовые функции и функции пакета "рио"

head(import("cardio_train.csv"))

install.packages("dplyr")
library(dplyr)
install.packages("rafalib")
library(rafalib)
# загружаем датасэт в R с помощью import() из пакета rio
dat <-import("cardio_train.csv")
head(dat)
# также получим дополнительные сведения о наборе данных с помощью dim() и str()
dim(dat)

str(dat)

#В столбце age  возраст представлен в днях, что не привычно. 
#Поэтому, для простоты интерпретации, добавим новый столбец, в котором возраст пациента будет в годах
?mutate

dat$age / 365
trunc(dat$age/365) # отсекает дробную часть
dat <-dat %>% mutate(age_years=(trunc(age/365))) # ф-ция  trunc() отсекает дробную часть

#добавили столбец "age_years"
head(dat)

min_weight <- min(dat$weight) #10
max_weight <- max(dat$weight) #200

#Воспользуемся функцией  filter(), %>%  из пакета dplyr ,чтобы подготовить датасэт без грубейших ошибок ввода

tidy_set <-dat %>% filter(weight<150&weight>45)

#после небольшой обработки данных взглянем на данные с помощью гистограммы

mypar(1,2)

hist(dat$weight, main="вес", xlab = "weight_dat", ylab="частота")
hist(tidy_set$weight, main="очищенный вес", xlab = "weight_tidy", ylab="частота")


# QQ-график позволяет проверить данные на нормальность
#в основе лежит идея сравнить теоретические квантили с квантилями случайной величины

mypar(1,1)
qqnorm(tidy_set$weight, main="вес.tidy")
qqline(tidy_set$weight, col="red", lwd=2)


#вывод: вес выше, чем предполагалось нормальным распределением по краям интервала
# и близок к нормальному распределению в диапазоне от 60 до 85 кг
how_much <- length((dat %>% filter(weight<=85&weight>=60))$weight) #это 48779 значений, т.е. ~2/3

#Сравним вес по полу

groupss_w<-split(tidy_set$weight,tidy_set$gender)

boxplot(groupss_w)
title("вес")

tidy_set_w = tidy_set %>% filter(gender==1)
tidy_set_m = tidy_set %>% filter(gender==2)

mypar(1,2)
plot(density(tidy_set_w$weight), col=1, lwd=2, main="вес женщин")
plot(density(tidy_set_m$weight), col=3, lwd=2, main="вес мужчин")

# пики в плотности вероятности появляются вероятнее всего из-за округления, 
# как и в случае с артериальным давлением

# КУРСОВОЙ ПРОЕКТ
#Проверить статистическую гипотезу о различии веса среди мужчин и женщин.
#Гипотеза H0 - нет статистически различимой разницы между весом мужчин и женщин
# H1 - есть.

#Выбрать критерий и обосновать его применение
mypar(1,2)
qqnorm(tidy_set_w$weight, main="вес женщин.tidy")
qqline(tidy_set_w$weight, col="red", lwd=2)

qqnorm(tidy_set_m$weight, main="вес мужчин.tidy")
qqline(tidy_set_m$weight, col="green", lwd=2)

# распределение близко к нормальному только в середине интервала значений
# объём выборок большой, стандартное отклонение неизвестно, выборки независимые
# поэтому используем t-тест двухвыборочный
# Предполагаем, что выборки с разной дисперсией - тест Уэлча


#С помощью изученных функций на 5 вебинаре рассчитать нужный объем выборки 
#для мощности теста 90%.
# α = 0.05

# посчитаем статистику d Коэна

install.packages("effsize")
library(effsize)
d<-cohen.d(tidy_set_m$weight,tidy_set_w$weight)$estimate

# d = 0.324

# почитаем мощность теста для выборок разного размера
install.packages("pwr")
library(pwr)
pwr.t2n.test(n1=length(tidy_set_m$weight),n2=length(tidy_set_w$weight),d=d,sig.level=0.05,alternative="two.sided")
# power = 1

#Предположим мы хотим обнаружить сильный эффект. Cohen`s  d  = 0.8
#Посчитаем объём выборок
pwr.t2n.test(n1=20, power=0.9,d=0.8,sig.level=0.05,alternative="two.sided")
# n2=101
pwr.t2n.test(n1=50,power=0.9,d=0.8,sig.level=0.05,alternative="two.sided")
# n2=26
pwr.t2n.test(n1=35, power=0.9,d=0.8,sig.level=0.05,alternative="two.sided")
# n2=33
pwr.t2n.test(n1=34, power=0.9,d=0.8,sig.level=0.05,alternative="two.sided")
# n2=34

#Провести тест и интерпретировать результат.
t.test(sample(tidy_set_m$weight,34),sample(tidy_set_m$weight,34),alternative="two.sided",var.equal = FALSE)


#Welch Two Sample t-test

#data:  sample(tidy_set_m$weight, 34) and sample(tidy_set_m$weight, 34)
#t = -0.51123, df = 65.171, p-value = 0.6109
#alternative hypothesis: true difference in means is not equal to 0
#95 percent confidence interval:
#  -10.101276   5.983629
#sample estimates:
#  mean of x mean of y 
#76.44118  78.50000 

#Вывод p-value = 0.6109 больше α = 0.05 => мы принимаем гипотезу об отсутствии 
#статистического различия веса мужчин и женщин
#Гипотеза Н0 верна на уровне значимости 0.05
#p-value = 0.6109
# доверительный интервал в  процентах
#  -10.101276   5.983629

