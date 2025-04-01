#ifndef CES12_ALUNOINDEXPOINTS_H
#define CES12_ALUNOINDEXPOINTS_H

#include <vector>
#include <map>
#include <IndexPointsAbstract.h>

class IndexPointsAluno : public IndexPointsAbstract {
    
public:
    
    IndexPointsAluno() : root(nullptr), siz(0) {}

    long size() ;
        
    void add (double key, long idx ) ;
    
    //look for a range of values
    void find(std::vector<long> &res, double first, double last) ;
    
    
private: 
    // ALUNO DEVE IMPLEMENTAR ALGO COM O MESMO COMPORTAMENTO DE MULTIMAP
    std::multimap<double, long> _map;
    enum co {BLACK, RED};
    struct node{
        double key;
        long index;
        co color;
        node *left, *right, *dad;
        node(double k, long i, co c, node *l, node *r, node *d): key(k), index(i), color(c), left(l), right(r), dad(d) {}
    };
    node *root;
    long siz;
    void insertFixup(node *n) ;
    void leftRotate(node *n) ;
    void rightRotate(node *n) ;
    void dfs(std::vector<long> &res, double first, double last, node *n) ;
    
};//class


#endif
