"""811. Subdomain Visit Count"""
class Solution:
    """Solution Class"""
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        """
        #This function calculates the number of visits for each subdomain and its parent domains.
        #Loom explanation: https://www.loom.com/share/907a5311a24b45aa91c24296188ae424
        """
        #To first create an hashmap where I will be tracking
        #for each domain/subdomain how many times gets visited.
        counts = {}
        #We will be iterating over the cpdoamins and start
        #assigning the respective
        #values to its respective domain.
        #Time Complexity O(k)
        for domain in cpdomains:
            count,domain = domain.split(" ")
            count = int(count)
            splittedDomains = domain.split(".")
            #Iterating over the splitted domains ~ subdomains
            #O(m)
            for i in range(len(splittedDomains)):
                #O(m)
                subdomain = ".".join(splittedDomains[i:])
                #Once we are able to access each indivudal subdomain
                #We can start populating our hashmap
                if subdomain in counts:
                    counts[subdomain] += count
                else:
                    counts[subdomain] = count
        #Time Complexity O(k) * O(m) * O(m) = O(k * m^2)
        #Space Complexity O(m)
        return [f"{count} {domain}" for domain, count in counts.items()]
