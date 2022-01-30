# https://docs.python.org/3/library/struct.html
import struct


# sdi is format for out data where ?-> Bool, d-> double, i->integer
# there are tons of formatting syntax that you can look into docs
student = struct.pack('?di',True,25.32,50_000)
print(f"before unpacking : {student}")

is_student, marks , fine = struct.unpack("?di",student)

print(is_student)
print(marks)
print(fine)

# N.B : for working with structure use NamedTuple or  DataClass because they are
# more convenient to use