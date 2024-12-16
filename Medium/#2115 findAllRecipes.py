class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]],
                       supplies: List[str]) -> List[str]:
        g = {}
        for r, i in zip(recipes, ingredients):
            g.setdefault(r, []).extend(i)

        supp = set(supplies)
        visited = set()

        @cache
        def dfs(item):
            if item in visited:
                return False

            visited.add(item)
            if item in supp:
                return True

            if item not in g:
                return False

            for required in g[item]:
                if not dfs(required):
                    return False

            supp.add(item)
            return True

        ans = []
        for recipe in recipes:
            if dfs(recipe):
                ans.append(recipe)

        return ans
