#coding:utf-8

class _const:
  class ConstError(TypeError): pass
  class ConstCaseError(ConstError): pass

  def __setattr__(self, name, value):
      if name in self.__dict__:
          raise self.ConstError("can't change const %s" % name)
      if not name.isupper():
          raise self.ConstCaseError('const name "%s" is not all uppercase' % name)
      self.__dict__[name] = value

const = _const()
'''
下面是一些常量

'''
# 储存中间图片的文件夹
const.INTER_RESULT_FOLDER = "../inter_result_picture/"

# 储存待识别的图片文件夹
const.IDENTIIFIED_PICTURE_FOLDER = "../identified_picture/"
