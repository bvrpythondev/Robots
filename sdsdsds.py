
# pip install pytransloadit
from transloadit import client

tl = client.Transloadit('YOUR_TRANSLOADIT_KEY', 'YOUR_TRANSLOADIT_SECRET')
assembly = tl.new_assembly()

assembly.add_step('imported_chameleon', {
  'robot': '/http/import',
  'result': True,
  'url': 'https://demos.transloadit.com/inputs/chameleon.jpg'
})
assembly.add_step('imported_prinsengracht', {
  'robot': '/http/import',
  'result': True,
  'url': 'https://demos.transloadit.com/inputs/prinsengracht.jpg'
})
assembly.add_step('imported_snowflake', {
  'robot': '/http/import',
  'result': True,
  'url': 'https://demos.transloadit.com/inputs/desert.jpg'
})
assembly.add_step('resized', {
  'use': ['imported_chameleon','imported_prinsengracht','imported_snowflake'],
  'robot': '/image/resize',
  'result': True,
  'height': 768,
  'imagemagick_stack': 'v2.0.3',
  'resize_strategy': 'fit',
  'width': 1024,
  'zoom': False
})
assembly.add_step('merged', {
  'use': {'steps':[{'name':':original','as':'audio'},{'name':'resized','as':'image'}],'bundle_steps':true},
  'robot': '/video/merge',
  'result': True,
  'duration': 9,
  'ffmpeg_stack': 'v3.3.3',
  'framerate': '1/3',
  'preset': 'ipad-high',
  'resize_strategy': 'fit'
})
assembly.add_step('exported', {
  'use': ['imported_chameleon','imported_prinsengracht','imported_snowflake','resized','merged',':original'],
  'robot': '/s3/store',
  'credentials': 'demo_s3_credentials'
})

# Add files to upload
assembly.add_file(open('./joakim_karud-rock_angel.mp3', 'rb'))

# Start the Assembly
assembly_response = assembly.create(retries=5, wait=True)

print(assembly_response.data.get('assembly_id'))

# or
print(assembly_response.data['assembly_id'])

