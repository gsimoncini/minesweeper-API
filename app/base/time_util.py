
def get_duration(started_at, finished_at):
    duration = finished_at - started_at
    duration_in_s = duration.total_seconds()
    days = divmod(duration_in_s, 86400)  # Get days (without [0]!)
    hours = divmod(days[1], 3600)  # Use remainder of days to calc hours
    minutes = divmod(hours[1], 60)  # Use remainder of hours to calc minutes
    seconds = divmod(minutes[1], 1)  # Use remainder of minutes to calc seconds
    return "%d:%d:%d" % ( hours[0], minutes[0], seconds[0])