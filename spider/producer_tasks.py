from tasks import tg_names_to_analyze

task_name = tg_names_to_analyze.delay("bitkogan")
print("Стартовал анализ ТГ-канала")