import survey
table = survey.Pregnancies()
table.ReadRecords()

class Birth_Order(object):

    def __init__(self):
        self.prgweeks = []

    def get_birth_count(self):
        return len(self.prgweeks)

    def get_avg_prg_weeks(self):
        return float(sum(self.prgweeks)) / self.get_birth_count()

birth_ord_list = [Birth_Order() for i in range(10)]

for record in table.records:
    if (record.outcome == 1): #outcome 1 indicates live birth
        birth_order = birth_ord_list[record.birthord - 1]
        birth_order.prgweeks.append(record.prglength)

if __name__ == "__main__":
    print "Number of Pregnancies", len(table.records)
    print "Number of live births", sum([bo.get_birth_count() for bo in birth_ord_list])
    print "Number of 1st borns", birth_ord_list[0].get_birth_count()
    print "Number of 2nd borns", birth_ord_list[1].get_birth_count()
    print '*' * 50
    for i, birth_order in enumerate(birth_ord_list):
        print "Average pregnancy length in weeks for child %d : %f" % (i+1, birth_order.get_avg_prg_weeks())
