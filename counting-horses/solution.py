def count_horses(sound_str):
    sound = [int(i) for i in sound_str]
    result = []

    for i in range(len(sound)):
        amount = sound[i]
        period = i + 1

        if amount == 0:
            continue

        for j in range(i + period, len(sound), period):
            sound[j] -= amount

        for _ in range(amount):
            result.append(period)

    return result
