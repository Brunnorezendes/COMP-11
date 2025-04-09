
#include <IndexPointsAluno.h>

/// returns the number of elements in the index
long IndexPointsAluno::size() { return siz; }

/// adds new element to the index. 
void IndexPointsAluno::add (double key, long idx ) {
    //_map.insert({key, idx});
    node *n = new node(key, idx, BLACK, nullptr, nullptr, nullptr);
    node *y = nullptr;
    node *x = root;
    while (x != nullptr){
        y = x;
        if (n->key < x->key)
            x = x->left;
        else
            x = x->right;
    }
    n->dad = y;
    if (y == nullptr)self.offset.x = player.rect.centerx - self.half_width
        root = n;
    else if (n->key < y->key)
        y->left = n;
    else
        y->right = n;
    n->left = nullptr;
    n->right = nullptr;
    siz++;
    if(n->dad == nullptr) return;
    n->color = RED;
    if(n->dad->dad==nullptr) return;
    insertFixup(n);
}


void IndexPointsAluno::find(std::vector<long> &res, double first, double last ) {
    /*auto itlow = _map.lower_bound (first);  // itlow points to first
  auto itup = _map.upper_bound (last);   // itup points to next after last (not to last)
  // print range [itlow,itup), which is the same as [itlow, last] or [first, last]
  for (auto it=itlow; it!=itup; ++it)
    //std::cout << (*it).first << " => " << (*it).second << '\n';
    res.push_back((*it).second);
    return;*/
    res.clear();
    dfs(res, first, last, root);
}//find

void IndexPointsAluno::insertFixup(node *n){
    while (n->dad != nullptr && n->dad->color == RED){
        if (n->dad->dad == nullptr) break;
        if (n->dad == n->dad->dad->left){
            node *y = n->dad->dad->right;
            if (y!=nullptr && y->color == RED){
                n->dad->color = BLACK;
                y->color = BLACK;
                n->dad->dad->color = RED;
                n = n->dad->dad;
            }
            else{
                if (n == n->dad->right){
                    n = n->dad;
                    leftRotate(n);
                }
                n->dad->color = BLACK;
                n->dad->dad->color = RED;
                rightRotate(n->dad->dad);
            }
        }
        else{
            node *y = n->dad->dad->left;
            if (y!=nullptr && y->color == RED){
                n->dad->color = BLACK;
                y->color = BLACK;
                n->dad->dad->color = RED;
                n = n->dad->dad;
            }
            else{
                if (n == n->dad->left){
                    n = n->dad;
                    rightRotate(n);
                }
                n->dad->color = BLACK;
                n->dad->dad->color = RED;
                leftRotate(n->dad->dad);
            }
        }
    }
    root->color = BLACK;
}

void IndexPointsAluno::leftRotate(node *n){
    if (n == nullptr || n->right == nullptr) return;
    node *y = n->right;
    n->right = y->left;
    if (y->left != nullptr)
        y->left->dad = n;
    y->dad = n->dad;
    if (n->dad == nullptr)
        root = y;
    else if (n == n->dad->left)
        n->dad->left = y;
    else
        n->dad->right = y;
    y->left = n;
    n->dad = y;
}

void IndexPointsAluno::rightRotate(node *n){
    if (n == nullptr || n->left == nullptr) return; 
    node *y = n->left;
    n->left = y->right;
    if (y->right != nullptr)
        y->right->dad = n;
    y->dad = n->dad;
    if (n->dad == nullptr)
        root = y;
    else if (n == n->dad->right)
        n->dad->right = y;
    else
        n->dad->left = y;
    y->right = n;
    n->dad = y;
}

void IndexPointsAluno::dfs(std::vector<long> &res, double first, double last, node *n){
    if(n==nullptr) return;
    if(n->key>first) dfs(res, first, last, n->left);
    if(n->key>first && n->key<last) res.push_back(n->index);
    if(n->key<last) dfs(res, first, last, n->right);
}