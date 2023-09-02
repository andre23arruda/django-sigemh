import io, qrcode, socket, sys
from django.core.files.uploadedfile import InMemoryUploadedFile

get_ip_address = lambda: socket.gethostbyname(socket.gethostname())


def generate_equipment_qrcode(equipment: object):
    '''Exibe qr code do participante'''
    site_url = f'http://{ get_ip_address() }:8000'
    # site_url = f'https://you-site-domain'
    img = qrcode.make(f'{ site_url }/equipments/{ equipment.id }/')
    buf = io.BytesIO()
    img.save(buf, 'PNG')
    buf.seek(0)

    qrcode_result = InMemoryUploadedFile(
        file=buf,
        field_name='ImageField',
        name=f'equipment_{equipment.patrimony}.png',
        content_type='image/png',
        size=sys.getsizeof(buf),
        charset=None
    )
    return qrcode_result
