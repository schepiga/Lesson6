from pymongo import MongoClient

# я сдаюсь. не смогла разбить зп:(((( хелп!

class VacancyparcerPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client['vacancies1508']

    def process_item(self, item: object, spider):
        if spider.name == 'hhru':
            salary_min = item['salary_min'].split(' ')
            salary_max = item['salary_max'].split(' ')
            salary_curr = item['salary_curr'].split(' ')
            if salary_min[0] == 'з/п':
                salary_min = None
                salary_max = None
                salary_curr = None
            elif salary_min is not None:
                salary_curr = salary_curr[-1]
            elif salary_min[0] == 'от':
                salary_min = int(''.join(salary_min[1].replace('\xa0', ' ')))
                salary_max = int(''.join(salary_min[3].replace('\xa0', ' ')))
            elif salary_min[0] == 'до':
                salary_min = int(''.join(salary_min[1].replace('\xa0', ' ')))
                salary_max = None
            else:
                salary_min = None
                salary_max = int(''.join(salary_min[1].replace('\xa0', ' ')))

            item['salary_min'] = salary_min
            item['salary_max'] = salary_max
            item['salary_curr'] = salary_curr

        collection = self.mongo_base[spider.name]
        collection.insert_one(item)

        return item




