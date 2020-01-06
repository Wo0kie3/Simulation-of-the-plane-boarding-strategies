from mesa.batchrunner import BatchRunner
from plane import PlaneModel
from statistics import mean

method_types = [
        'Random',
        'Front-to-back',
        'Front-to-back (4 groups)',
        'Back-to-front',
        'Back-to-front (4 groups)',
        'Window-Middle-Aisle',
        'Steffen Perfect',
        'Steffen Modified'
    ]

#fixed_params = {"method": "Front-to-back"}
#batch_run = BatchRunner(PlaneModel, None, fixed_params, iterations=100)
#batch_run.run_all()
for i in method_types:
    fixed_params = {"method": i}
    batch_run = BatchRunner(PlaneModel, None, fixed_params, iterations=100,
                            model_reporters={"method_time": lambda m: m.schedule.time}, display_progress=False)
    batch_run.run_all()
    average_time = mean(batch_run.get_model_vars_dataframe()['method_time'])
    print("{}: {}".format(i, average_time))
