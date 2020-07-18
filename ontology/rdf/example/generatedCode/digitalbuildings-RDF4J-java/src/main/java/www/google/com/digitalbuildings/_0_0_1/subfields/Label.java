package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Label 
* Identifying alias for component or system.
*/
@SuppressWarnings("serial")
public class Label extends www.google.com.digitalbuildings._0_0_1.subfields.Point_type implements ILabel{

	IRI newInstance;
	public Label(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Label"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ILabel> getAllLabelsObjectsCreated(){
		Set<ILabel> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Label")).subjects().stream()
		.map(mapper->(ILabel)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}