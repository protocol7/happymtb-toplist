import re
import httplib

PROFILE_PATTERN = re.compile(r'.*\"(\d+).*>(.*?)<.*')
POSTS_PATTERN = re.compile(r'gg:</td><td>([\d,]+)')

client = httplib.HTTPConnection('happymtb.org')

def get_post_count(user_id):
    client.request('GET', '/forum/profile.php/1/%s' % id)
    r1 = client.getresponse()

    return int(POSTS_PATTERN.findall(r1.read())[0].replace(",", ""))

# users.txt contains the <options> elements from the "Send private message"
# page on happymtb.org
with open("users.txt") as f:
  users = [PROFILE_PATTERN.findall(line)[0] for line in f if line.strip()]
  posts = []

  for c, (id, name) in enumerate(users):
    if c % 100 == 0: print("%d / %d" % (c, len(users)))
    posts.append((get_post_count(id), name))

  posts = sorted(posts, reverse=True)
  for i, (count, user) in enumerate(posts):
      print "%5s %-20s %s" % (i+1, user, count)
