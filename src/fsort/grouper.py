from pathlib import Path
from fsort.strategies import registry

def group_files(files):

    StrategyList = [strgy_ins() for strgy_ins in registry.StrategyList]
    Key_List = []
    for strategy in StrategyList:
        #print(type(strategy.group_name))
        has_group_name = hasattr(strategy, "group_name")
        group_name = getattr(strategy, "group_name", None)
        if not has_group_name:
            raise AttributeError(f"{type(strategy).__name__}: group_name must exist!")
        elif type(group_name) != str:
            raise AttributeError(f"{type(strategy).__name__}: group_name should be a string datatype!")
        elif group_name.strip() == "":
            raise AttributeError(f"{type(strategy).__name__}: group_name cannot be empty!")
        if strategy.group_name in Key_List:
            raise AttributeError(f"{type(strategy).__name__}: Duplicates found!!!. group_name: {strategy.group_name} is already in other strategy!")
        else:
            Key_List.append(strategy.group_name)
    c = 0
    Fall_Back = None
    dummy_path = Path('/tmp/data.bin')
    for Fall_strategy in StrategyList:
        if Fall_strategy.accepts(dummy_path):
            c += 1
            Fall_Back = Fall_strategy
    if c == 0:
            raise AttributeError(f"{type(strategy).__name__} : No fallback")
    elif c > 1:
            raise AttributeError(f"{type(strategy).__name__} : Multiple fallbacks")
    elif StrategyList[-1] != Fall_Back:
            raise AttributeError(f"{type(strategy).__name__} : Fallback must be last in order.")

    Val_List = [[] for strgy in Key_List]
    group = dict(zip(Key_List, Val_List))

    #print(group)
    #print(files)
    for file in files:
        #print(file)
        for obj in StrategyList:
            result = obj.accepts(file)
            if isinstance(result,bool) and result:
                group[obj.group_name].append(file)
                break
    #print(group)
    return group

