def compute_lps_array(pattern):

  m = len(pattern)
  lps = [0] * m

  i = 1
  j = 0
  while i < m:
    if pattern[i] == pattern[j]:
      lps[i] = j + 1
      i += 1
      j += 1
    else:
      if j != 0:
        j = lps[j - 1]
      else:
        lps[i] = 0
        i += 1
  return lps

def kmp_search(text, pattern):

  n = len(text)
  m = len(pattern)
  lps = compute_lps_array(pattern)

  i = 0  # index for text
  j = 0  # index for pattern
  matches = []
  while i < n:
    if text[i] == pattern[j]:
      i += 1
      j += 1
    if j == m:
      matches.append(i - m)
      j = lps[j - 1]  # Shift the pattern using LPS
    elif i < n and text[i] != pattern[j]:
      if j != 0:
        j = lps[j - 1]
      else:
        i += 1
  return matches

# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

matches = kmp_search(text, pattern)

if matches:
  print("Pattern found at indices:", matches)
else:
  print("Pattern not found in the text")
