import shutil

shutil.copy('video/variants/phone_680p_crf38.webm', 'video/phone_members.webm')
shutil.copy('video/variants/phone_680p_crf26.mp4', 'video/phone_members.mp4')
shutil.copy('video/variants/phone_540p_crf38.webm', 'video/phone_members_mob.webm')
shutil.copy('video/variants/phone_540p_crf26.mp4', 'video/phone_members_mob.mp4')

print("Copied production video files.")
