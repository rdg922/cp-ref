typedef pair<int, pair<int, int>> Edge; // {weight, {vertex1, vertex2}}

int kruskal(int n, vector<Edge> &edges) {
  DSU dsu(n);
  sort(edges.begin(), edges.end()); // sort by weight
  int totalWeight = 0;
  for (const auto &edge : edges) {
    int weight = edge.first;
    int u = edge.second.first;
    int v = edge.second.second;
    if (!dsu.sameSet(u, v)) {
      dsu.join(u, v);
      totalWeight += weight;
    }
  }
  return totalWeight;
}
