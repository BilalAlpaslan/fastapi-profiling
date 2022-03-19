from multiprocessing import freeze_support
import yappi
import main

yappi.set_clock_type("CPU")

with yappi.run():
    main.main()

freeze_support()
stats = yappi.get_func_stats()
stats.save("fastapi_profiler.callgrind", type="CALLGRIND")
stats.print_all()