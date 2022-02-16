# Write your code here
def cakes(eggs,butter,flour):
    ##Do NOT rely on floor in your translation
    ##Use integer division as explained below
    maxByEggs = eggs // 5
    maxByButter = butter // 250
    maxByFlour = flour // 5

    return min(maxByEggs, maxByButter, maxByFlour)