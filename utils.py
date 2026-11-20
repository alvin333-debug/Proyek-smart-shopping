"""Fungsi bantuan aplikasi."""
def format_rupiah(value):
    return "Rp " + f"{int(value):,}".replace(",", ".")

def parse_integer(value, field_name, minimum=0):
    try:
        number = int(value)
    except (ValueError, TypeError):
        raise ValueError(f"{field_name} harus berupa angka bulat.")
    if number < minimum:
        raise ValueError(f"{field_name} minimal {minimum}.")
    return number
