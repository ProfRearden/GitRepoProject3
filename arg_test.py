import os
import sys


# print('INCOMING FROM GITHUB: %s  %s' % (sys.argv[2], sys.argv[3:]))
#
#print(sys.argv)
#
#print(sys.argv[1], sys.argv[2:])
stripped = [s.strip('\\r') for s in sys.argv[3:]]
print(sys.argv[1])


#argument_2 = ' '.join(*(sys.argv[3:].strip("\r")).replace('\r','').split())
# print(argument_2)


# my_list = ['this\n', 'is\n', 'a\n', 'list\n', 'of\n', 'words\n']
# stripped = [s.strip('\n') for s in my_list]
# print(*stripped)

#print(len(sys.argv))
#run(sys.argv[1], (*(sys.argv[2:])))
#run()
#print('INCOMING FROM GITHUB: %s' % sys.argv[1])
#run: python software_release_protocol.py ${{ github.event.release.name}}
#run: python software_release_protocol.py ${{ github.event.release.tag_name}}
