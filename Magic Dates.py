from datetime import date, timedelta
#verifica o range de datas disponíveis.
def dateRange(begin, end):
    for n in range(int ((end - begin).days)+1): yield begin + timedelta(n)
def isMagicDate(date):
  #faz o cálculo para verificar se é uma Magic Date
    if(date.day * date.month == (int(str(date.year)[2:]))): print(date.strftime("%Y-%m-%d")," is a Magic Date")
def main():
  #seta o inicio da data para o começo do século e o final para a data final.
    beginDate = date(1901,1,1)
    endDate = date(1999,12,31)
    for dates in dateRange(beginDate, endDate): isMagicDate(dates)
main()