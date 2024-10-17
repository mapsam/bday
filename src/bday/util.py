def build_dt(**kwargs):
    d = str(kwargs.get("day")).zfill(2)
    m = str(kwargs.get("month")).zfill(2)
    return f"{m}:{d}"