struct node {
  vector<node *> ch;
  bool isWord = false;
  int cnt = 0;

  node() { ch = vector<node *>(26, nullptr); }

  void insert(string &s, int idx) {
    cnt++;
    if (idx == sz(s)) {
      isWord = true;
      return;
    }
    int edge = s[idx] - 'a';
    if (!ch[edge])
      ch[edge] = new node();
    ch[edge]->insert(s, idx + 1);
  }

  bool find(string &s, int idx) {
    if (idx == sz(s))
      return isWord;
    int edge = s[idx] - 'a';
    if (!ch[edge])
      return false;
    return ch[edge]->find(s, idx + 1);
  }

  int count(string &s, int idx) {
    if (idx == sz(s))
      return cnt;
    int edge = s[idx] - 'a';
    if (!ch[edge])
      return 0;
    return ch[edge]->count(s, idx + 1);
  }
};
