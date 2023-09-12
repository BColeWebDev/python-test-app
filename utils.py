# Sorts workouts by asc or desc
import json


def Sortation(sort, workouts):

    key = sort.split(':')[0]
    value = sort.split(':')[1]

    if (value == "asc"):
        workouts = sorted(workouts, key=lambda d: d[f'{key}'])
        return workouts

    if (value == "desc"):
        workouts = sorted(workouts, key=lambda d: d[f'{key}'], reverse=True)
        return workouts


def Pagination(page, pageDisplay, workouts):
    startIndex = (page - 1)*pageDisplay
    endIndex = page * pageDisplay
    results = workouts[startIndex:endIndex]
    return results


def Filtering(filters, workouts):
    all_filters = dict(json.loads(filters))
    print(list(all_filters.keys())[0])

    # workouts = list(
    #     filter(lambda sub: sub["bodyPart"] == "chest", workouts))
    workouts = [
        workout for workout in workouts if list(all_filters.values())[0] in workout[f"{list(all_filters.keys())[0]}"]]
    return workouts
