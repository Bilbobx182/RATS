const GET_USERS = gql`
{
  allLocations {
  edges {
    node {
      id,city
    }
  }
}
}
`

const Location = ({ item: { city } }) => (
  <div className="Location">
    <h1 className="Location--name">{city}</h1>
  </div>
)

