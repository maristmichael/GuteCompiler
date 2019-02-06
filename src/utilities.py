def parsePrograms(input_):
    eop_count = input_.count('$')
    programs = input_.split('$')
    program_count = len(programs)

    if eop_count is 0 or eop_count != program_count:
        print("Warning: Missing EOP '$'")

    return programs
