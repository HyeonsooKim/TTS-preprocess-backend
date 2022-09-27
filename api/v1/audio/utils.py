from apps.audio.models import Audio

def create_audio(project, li):
    """ 오디오 생성 함수 """
    res = []

    # audio 객체 생성
    for i, txt in enumerate(li):
        audio = Audio.objects.create(
            audio_id=i + 1,
            text=txt,
            project=project
        )
        res.append((audio.id, audio.text))

    return res