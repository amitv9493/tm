
def get_ids( date_obj, *args, **kwargs):
    if kwargs["ttd"] == 1:
        return 'ttd'



print(get_ids(date_obj=1,ttd=1))