from PIL import ImageFilter
from PIL import Image

"""#텔레포트 만들기
천재 과학자 민영이는 영화를 좋아해서, 외부의 물체를 브라운 관 안의 세계로 전송하는 텔레포트 기계를 만들고자 한다.<br>
수차례 실험을 거듭한 결과, 민영이는 텔레포트 기계를 만들어냈다.<br>
다만, 현대 기술의 한계로 텔레포트로 전송된 물체는 디지털 세계에서 원래 크기보다 10배 작아지고, 좌우반전이 된 상태로 전송이 되어버리고 만다.<br>
<br>
민영이가 만든 텔레포트를 구현하는 함수를 짜보자!<br>


"""

def teleport():
  img = Image.open('chocolate.jpg')
  size = (img.size[0]//10, img.size[1]//10)
  
  ###code here ###
  img = img.resize(size)
  def Choose_type():
    while True:
        type = int(input("choose filter (1: blur, 2: edge_enhance, 3: emboos, 4: gray): "))
        return type

  type = Choose_type()
  if type == 1:
      img = img.filter(ImageFilter.BLUR)
  elif type == 2:
      img = img.filter(ImageFilter.EDGE_ENHANCE)
  elif type == 3:
      img = img.filter(ImageFilter.EMBOSS)
  elif type == 4:
      img = img.convert('L')
  ################
  img.save('img.jpeg')

if __name__ =="__main__":
  teleport()
