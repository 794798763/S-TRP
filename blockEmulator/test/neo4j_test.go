package test

import (
	"context"
	"github.com/neo4j/neo4j-go-driver/v5/neo4j"
)

func makeTxGraphInNeo4j() {
	dburl := "neo4j://localhost:7687"
	driver, err := neo4j.NewDriverWithContext(dburl, neo4j.BasicAuth("neo4j", "lwq123456", ""))
	if err != nil {
		panic(err)
	}
	ctx := context.Background()
	defer driver.Close(ctx)

}

type Node struct {
	Id   int64
	Name string
}

type Edge struct {
	Id   int64
	Name string
}
