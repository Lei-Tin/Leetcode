class Solution:
    def maximumTime(self, time: str) -> str:
        new_time = ''

        for i in range(len(time)):
            if time[i] == '?':
                # If we are at the tens place of the hour
                if i == 0:
                    if time[i + 1] in '?0123':
                        new_time += '2'
                    else:
                        new_time += '1'

                # Ones place of the hour
                if i == 1:
                    if new_time[0] == '2':
                        new_time += '3'
                    else:
                        new_time += '9'

                # Tens place of the minute
                if i == 3:
                    new_time += '5'

                # Ones place of the minute
                if i == 4:
                    new_time += '9'
            else:
                new_time += time[i]

        return new_time
