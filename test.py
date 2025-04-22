# AG

# setup initial population and setup initial best solution ( keep building random instances, check if its valid and then append it until we have the pop size)

# while stop_critetia is not met
    # do crosses and mutations and keep best solution


#### crosses and mutations

# build roulete by iterating over all indvs and append to list acc OF

# then for every crossing num ( N * Tc  / 2 times)

    # select a random indv by getting a randint between 0 and total acc OF and running a bin search to find nearest/lower or equal value on acc list ( one time for each indv)


    # (does it have to check if new instances are valid ?)
    # then select the genes that are going to be crossed and swap them ( update parents in place to build children)
    # note: keep building crossings until both children are valid (<= 15 KG) and then update parents positions in place 
    # rand select the genes that are going to be crossed 
    # build children by swapping these values
    # eval children and if both are valid, break loop update on parents positions


    # (does it have to check if new instance is valid ?)
    # rand prob if mutate
    # rand select the indv that is going to be mutated 
    # rand select the gene that is going to be mutated
    # rand select the value that the gene will have
    # eval solution and break loop update if valid instance
    # note: keep building mutation of the indv until it is valid (<= 15 KG) and then update it in place




    # at last, check if any of the new indvs have better score than curr best



###### functions
# stop_criteria
# reproduce (build roullete, then cross and mutate indvs)
# build_roullete
# cross
# mutate
# valid_instance

