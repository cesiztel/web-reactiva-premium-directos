<?php 

class MysqlQueryBuilder
{
    private $query;

    public function select(string $table, array $fields)
    {
        $this->query = new \stdClass();
        $this->query->base = "SELECT " . implode(", ", $fields) . " FROM " . $table;
        $this->query->type = 'select';
    }

    public function where(string $field, string $value, string $operator = '=')
    {
        if (!in_array($this->query->type, ['select', 'update', 'delete'])) {
            throw new \Exception("WHERE can only be added to SELECT, UPDATE OR DELETE");
        }
        $this->query->where[] = "$field $operator '$value'";
    }

    public function limit(int $start, int $offset)
    {
        if (!in_array($this->query->type, ['select'])) {
            throw new \Exception("LIMIT can only be added to SELECT");
        }
        $this->query->limit = " LIMIT " . $start . ", " . $offset;
    }

    // ... muchos otros metodos

    public function getSQL(): string
    {
        $query = $this->query;
        $sql = $query->base;
        if (!empty($query->where)) {
            $sql .= " WHERE " . implode(' AND ', $query->where);
        }
        if (isset($query->limit)) {
            $sql .= $query->limit;
        }
        $sql .= ";";
        return $sql;
    }
}

function clientCode(MysqlQueryBuilder $queryBuilder)
{
    // ...
    $queryBuilder->select("users", ["name", "email", "password"]);
    $queryBuilder->where("age", 18, ">");
    $queryBuilder->where("age", 30, "<");
    $queryBuilder->limit(10, 20);
    $query = $queryBuilder->getSQL();

    echo $query;

    // ...
}

echo "Testing MySQL query builder:\n";
clientCode(new MysqlQueryBuilder());