#include <stdio.h>
#include <stdlib.h>
struct node
{
    int data;
    struct node* left;
    struct node* right;
};
void insert(struct node** root, int data);
void preOrder(struct node* root);
void inOrder(struct node* root);
void postOrder(struct node* root);
int size(struct node* root);
int height(struct node* root);
int sumOfWeight(struct node* root);
int maxPathWeight(struct node* root);
void mirror(struct node** root);
void destruct(struct node** root);
int main()
{
    int numTestCases;
    scanf("%d", &numTestCases);
    while (numTestCases--)
    {
        int num, i;
        struct node* root = NULL;
        scanf("%d", &num);
        for (i = 0; i < num; i++)
        {
            int data;
            scanf("%d", &data);
            insert(&root, data);
        }
        printf("%d\n", size(root));
        printf("%d\n", height(root) - 1); 
        printf("%d\n", sumOfWeight(root)); 
        printf("%d\n", maxPathWeight(root)); 
        mirror(&root);
        preOrder(root); printf("\n");
        inOrder(root); printf("\n");
        postOrder(root); printf("\n");
        destruct(&root); // BST의 모든 노드의 동적 메모리 해제
        if (root == NULL)
            printf("0\n");
        else
            printf("1\n");
    }
    return 0; 
}
// 데이터 삽입(recursion)
void insert(struct node** root, int data) {
    struct node *tmp = *root;
    if(tmp == NULL){
        tmp = new node;
        tmp->data = data;
        tmp->left = NULL;
        tmp->right = NULL;
    }
    else if(data < tmp->data){
        insert(&tmp->left, data);
    }
    else {
        insert(&tmp->right, data);
    }
    *root = tmp;
}
// 전위(preorder)탐색(recursion) 
void preOrder(struct node* root) {
    if(root == NULL)
        return;
    else
        printf("%d ", root->data);
        preOrder(root->left);
        preOrder(root->right);
}
// 중위(inorder)탐색(recursion) 
void inOrder(struct node* root) {
    if(root == NULL){
        return;
    }
    else{
        inOrder(root->left);
        printf("%d ", root->data);
        inOrder(root->right);
    }
}
// 후위(postorder)탐색(recursion)
void postOrder(struct node* root) {
    if(root == NULL)
        return;
    else{
        postOrder(root->left);
        postOrder(root->right);
        printf("%d ", root->data);
    }

}
// 노드의 개수(recursion) 
int size(struct node* root) {
    if(root == NULL){
        return 0;
    }
    else{
        return size(root->left) + size(root->right) + 1;
    }
}
// 높이(recursion)
int height(struct node* root) {
    if(root == NULL){
        return 0;
    }
    else{
        int leftheight, rightheight;
        leftheight = height(root->left);
        rightheight = height(root->right);
        return 1 + (leftheight >= rightheight ? leftheight : rightheight);
    }
}
// 미러 이미지로 변환하기(recursion) 
void mirror(struct node** root)
{   struct node *tmp = *root;
    if(tmp == NULL)
        return;
    else{
        mirror(&tmp->left);
        mirror(&tmp->right);

        struct node* temp;
        temp = tmp->left;
        tmp->left = tmp->right;
        tmp->right = temp;
    }
}
// 노드에 저장된 데이터의 값의 합 구하기(recursion) 
int sumOfWeight(struct node* root)
{
    if(root == NULL){
        return 0;
    }
    else{
        int leftweight, rightweight;
        leftweight = sumOfWeight(root->left);
        rightweight = sumOfWeight(root->right);
        return (leftweight + rightweight) + root->data;
    }
}
// 루트노드부터 단말노드까지의 경로 상의 데이터의 최대합(recusrion) 
int maxPathWeight(struct node* root)
{
    if(root == NULL)
        return 0; 
    else {
        int leftWeight, rightWeight;
        leftWeight = maxPathWeight(root->left);
        rightWeight = maxPathWeight(root->right);
        return root->data + (leftWeight >= rightWeight ? leftWeight : rightWeight); 
    }
}
// 트리노드의 동적 메모리 해제하기(recursion) 
void destruct(struct node** root)
{   struct node *tmp = *root;
    if(tmp == NULL){
        return;
    }
    else{
        destruct(&tmp -> left);
        destruct(&tmp -> right);
        tmp = NULL;
    }
    *root = tmp;
}