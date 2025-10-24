import csv

class CreatureRankingSystem:
    def __init__(self):
        self.creatures = []
        self.scores = {}

    def load_creatures(self, filename):
        """Carrega os dados dos animais do CSV."""
        self.creatures = []
        with open(filename, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                creature = (
                    row['Animal'],
                    float(row['Fofura']),
                    float(row['Ameaça']),
                    float(row['Insanidade']),
                    float(row['Tamanho']),
                    float(row['Habilidade']),
                    float(row['Comédia'])
                )
                self.creatures.append(creature)
        self.scores = {name: 0 for name, *_ in self.creatures}

    def load_user_weights(self):
        """Lê os pesos dos usuários do input padrão."""
        filename = input().strip()
        num_users = int(input())
        user_weights = []
        for _ in range(num_users):
            weights = list(map(float, input().strip().split()))
            user_weights.append(weights)
        return filename, user_weights

    def calculate_scores(self, weights):
        """Calcula os scores usando números de ponto flutuante."""
        scores = []
        for name, *attrs in self.creatures:
            score = sum(a * w for a, w in zip(attrs, weights))
            scores.append((score, name))
        return scores

    def merge_sort(self, arr, compare_func):
        """Implementação do Merge Sort com função de comparação personalizada."""
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid], compare_func)
        right = self.merge_sort(arr[mid:], compare_func)
        
        return self.merge(left, right, compare_func)

    def merge(self, left, right, compare_func):
        """Função de merge para o Merge Sort com comparação personalizada."""
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if compare_func(left[i], right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def compare_creatures(self, a, b):
        """Função de comparação para score (decrescente) e nome (crescente)."""
        if a[0] != b[0]:  # Se os scores são diferentes
            return a[0] > b[0]  # Ordena por score decrescente
        else:
            return a[1] < b[1]  # Desempate por nome crescente

    def rank_scores(self, scores):
        """Ordena os scores com desempate lexicográfico."""
        return self.merge_sort(scores, self.compare_creatures)

    def process_user_rankings(self, user_weights):
        """Processa os rankings de todos os usuários."""
        for weights in user_weights:
            scores = self.calculate_scores(weights)
            ranking = self.rank_scores(scores)
            points = len(ranking) - 1
            for name in ranking:
                self.scores[name[1]] += points
                points -= 1

    def generate_final_ranking(self):
        """Gera o ranking final com desempate por nome."""
        final_ranking = [(score, name) for name, score in self.scores.items()]
        return self.merge_sort(final_ranking, self.compare_creatures)

    def run(self):
        filename, user_weights = self.load_user_weights()
        self.load_creatures(filename)
        self.process_user_rankings(user_weights)
        final_ranking = self.generate_final_ranking()
        for score, name in final_ranking:
            print(f"{name} {score}")

if __name__ == "__main__":
    ranking_system = CreatureRankingSystem()
    ranking_system.run()