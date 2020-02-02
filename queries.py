from gql import gql


def get_profile():
    query = '''
        query{
              profiles{
                    edges{
                          node{
                            id
                            discordId
                            expEarned
                          }
                    }
              }
        }
    '''
    return gql(query)