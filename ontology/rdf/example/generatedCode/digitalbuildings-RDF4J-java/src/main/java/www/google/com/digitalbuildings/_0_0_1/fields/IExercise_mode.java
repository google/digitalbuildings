package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IExercise;
import www.google.com.digitalbuildings._0_0_1.subfields.IMode;

public interface IExercise_mode extends IField{

	public IRI iri();

    public void addComposedOfExercise (IExercise parameter);

	public Set<IExercise> getComposedOfExercise();

    public void addComposedOfMode (IMode parameter);

	public Set<IMode> getComposedOfMode();

}