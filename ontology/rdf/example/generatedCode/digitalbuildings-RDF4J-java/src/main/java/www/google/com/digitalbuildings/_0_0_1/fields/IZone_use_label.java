package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IUse;
import www.google.com.digitalbuildings._0_0_1.subfields.IZone;
import www.google.com.digitalbuildings._0_0_1.subfields.ILabel;

public interface IZone_use_label extends IField{

	public IRI iri();

    public void addComposedOfLabel (ILabel parameter);

	public Set<ILabel> getComposedOfLabel();

    public void addComposedOfUse (IUse parameter);

	public Set<IUse> getComposedOfUse();

    public void addComposedOfZone (IZone parameter);

	public Set<IZone> getComposedOfZone();

}