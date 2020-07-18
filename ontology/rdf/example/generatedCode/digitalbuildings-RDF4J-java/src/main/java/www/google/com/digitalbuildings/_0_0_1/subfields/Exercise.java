package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Exercise 
* Mode of running equipment to maintain functionality ('exercise mode')
*/
@SuppressWarnings("serial")
public class Exercise extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IExercise{

	IRI newInstance;
	public Exercise(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Exercise"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IExercise> getAllExercisesObjectsCreated(){
		Set<IExercise> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Exercise")).subjects().stream()
		.map(mapper->(IExercise)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}