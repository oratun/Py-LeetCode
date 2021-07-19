from typing import List

from node import TreeNode

'''
class Solution {
public:
    vector<vector<int>> BSTSequences(TreeNode* root) {
        if (!root) return {{}};
        deque<TreeNode*> q;
        q.push_back(root);
        vector<int> buf;
        vector<vector<int> > ans;
        Inner(q, buf, ans);
        return ans;
    }
    void Inner(deque<TreeNode*> &q, vector<int> &buf, vector<vector<int> > &ans) {
        if (q.empty()) {
            ans.push_back(buf);
            return;
        }
        int size = q.size();
        while (size--) {
            TreeNode *r = q.front(); q.pop_front();
            buf.push_back(r->val);
            int children = 0;
            if (r->left) {
                ++children;
                q.push_back(r->left);
            }
            if (r->right) {
                ++children;
                q.push_back(r->right);
            }
            Inner(q, buf, ans);
            while (children--) {
                q.pop_back();
            }
            q.push_back(r);
            buf.pop_back();
        }
    }
};
'''


class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        # if not root:
        #     return [[]]
        # q = [root]
        # buf = []
        # ans = []
        #
        # def dfs(q, buf, ans):
        #     if not q:
        #         ans.append(buf[:])
        #         return
        #     for i in range(len(q)):
        #         node = q.pop(0)
        #         buf.append(node.val)
        #         children = 0
        #         if node.left:
        #             children += 1
        #             q.append(node.left)
        #         if node.right:
        #             children += 1
        #             q.append(node.right)
        #         dfs(q, buf, ans)
        #         for j in range(children):
        #             q.pop(-1)
        #         q.append(node)
        #         buf.pop(-1)
        #
        # dfs(q, buf, ans)
        # return ans

        if not root:
            return [[]]
        res = []

        def dfs(root: TreeNode, q: list, path: list):
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
            if not q:
                res.append(path)
            for i in range(len(q)):
                dfs(q[i], q[0:i] + q[i + 1:], path + [q[i].val])

        dfs(root, [], [root.val])
        return res


if __name__ == '__main__':
    t = TreeNode(2)
    t.left = TreeNode(1)
    t.right = TreeNode(3)

    # [5, 2, null, 1, 4, null, null, 3]

    s = Solution()
    r = s.BSTSequences(t)
    print(r)
