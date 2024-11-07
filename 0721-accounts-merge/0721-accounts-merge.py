from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(set) # undirected graph
        for account in accounts:
            name, *emails = account
            representing = emails[0] # representing is x
            for email in emails: # email is y
                graph[representing].add(email)
                graph[email].add(representing)
        
        seen = set()
        def dfs(root):
            accounts = [root]
            stack = [root]
            while stack:
                node = stack.pop()
                seen.add(node)
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
                        accounts.append(neighbor)
            accounts.sort()
            return accounts

        ans = []
        for account in accounts:
            name, *emails = account
            for email in emails:
                if email not in seen:
                    merged_accounts = dfs(email)
                    ans.append([name] + merged_accounts)
        return ans